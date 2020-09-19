"""
name: query_by_sequence.py

usage: query_by_sequence.py sequence_file 

commissioned by : Dr. Makoto Saito, 2013-03

authorship: adorsk, 2013-05
updated: Jaclyn Saunders, 2020-09

description: This script queries a peptides database for the given set of
peptide sequences.

Outputs: a CSV document to stdout whose rows contains:
    query_sequence | taxon_id | match_sequence | count_in_taxon
"""

"""
Imports and setup.
"""
from proteomics import db
from proteomics import config
from proteomics.models import (Peptide, TaxonDigestPeptide, TaxonDigest)
import argparse
import logging
import os
from sqlalchemy.sql import func

"""
Process arguments.
"""
argparser = argparse.ArgumentParser(description=(
    'Query database for peptide sequences'))
argparser.add_argument('--sequence-file', help=(
    'File containing one amino acid sequence per line.'))

argparser.add_argument('--sequence', help='Amino acid sequence')

"""
Main method.
"""
def main():
    args = argparser.parse_args()
    print args

    logger = logging.getLogger('query_by_sequence')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)

    connection = db.get_connection()
    session = db.get_session(bind=connection)

    # Read in sequences to query.
    sequences = []
    if args.sequence_file:
        with open(args.sequence_file, 'rb') as f:
            sequences = [line.strip() for line in f.readlines()]
    elif args.sequence:
        sequences = [args.sequence]

    if not sequences:
        argparser.error("Provide a query sequence via the '--sequence' option, "
                        "or a set of sequences via the --sequence-file option")

    # Print headers. 
    headers = ['query', 'taxon', 'match', 'count']
    print ','.join(headers)

    # Execute query for each sequence and print results.
    for seq in sequences:
        q = (session.query(TaxonDigest.taxon_id, 
                           Peptide.sequence, TaxonDigestPeptide.count)
             .select_from(Peptide)
             .join(TaxonDigestPeptide)
             .join(TaxonDigest)
             .filter(Peptide.sequence == seq)
            )
        for row in q:
            print ','.join([str(s) for s in [seq] + list(row)])

if __name__ == '__main__':
    main()

