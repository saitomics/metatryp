*NOTE:* This documentation is currently in progress and is incomplete.

# METATRYP v. 2.0 Documentation
These tools are intended to help researchers answer questions about proteomics data. Written in Python 3.6 on a Unix operating system (linux/macOS).

METATRYP v. 2.0 is a revised and expanded from METATRYP v. 1.0 found here: http://github.com/saitomics/metatryp

METATRYP v. 2.0 now supports the ingestion and search of Genomes, Single Amplified Genomes (SAGs) and Metagenome Assembled Genomes (MAGs), Metagenome & Metatranscriptomic assemblies. This repository is designed both to be used as a stand alone application and in support of the Ocean Protein Portal (http://proteinportal.whoi.edu). 

The METATRYP analysis tools consist of:
1. a database, stored in a postgreSQL database.
2. python libraries, for processing, ingesting, and analyzing data. 
3. command-line scripts, to act as interfaces to the python libraries and the database.

***

* [Overview](https://github.com/WHOIGit/metatryp-2.0/wiki/Overview)
* [Installation Instructions](https://github.com/WHOIGit/metatryp-2.0/wiki/Installation-Instructions)
    * [Download](https://github.com/WHOIGit/metatryp-2.0/wiki/Installation-Instructions#1-download-this-repository-follow-a-or-b)
    * [Create virtual environment](https://github.com/WHOIGit/metatryp-2.0/wiki/Installation-Instructions#2-create-a-virtual-environment-follow-a-or-b)
    * [Run tests](https://github.com/WHOIGit/metatryp-2.0/wiki/Installation-Instructions#3-run-tests)
    * [Initialize database](https://github.com/WHOIGit/metatryp-2.0/wiki/Installation-Instructions#4-initialize-the-sqlite-database-follow-a-or-b)
* [Quick Usage Guide](https://github.com/WHOIGit/metatryp-2.0/wiki/Quick-Usage-Guide)
    * [Digest and ingest new taxa](https://github.com/WHOIGit/metatryp-2.0/wiki/Quick-Usage-Guide#1-digest-and-ingest-data)
    * [Generate peptide redundancy tables](https://github.com/WHOIGit/metatryp-2.0/wiki/Quick-Usage-Guide#2-generate-redundancy-tables)
    * [Remove taxa from database](https://github.com/WHOIGit/metatryp-2.0/wiki/Quick-Usage-Guide#3-remove-taxa-from-the-database)
* [Tutorial](https://github.com/WHOIGit/metatryp-2.0/wiki/Tutorial)
    * [Taxa in Example Database](https://github.com/WHOIGit/metatryp-2.0/wiki/Tutorial/_edit#taxa-in-database)
* [Database Schema](https://github.com/WHOIGit/metatryp-2.0/wiki/Database-Schema)
* [Directly query database via SQL](https://github.com/WHOIGit/metatryp-2.0/wiki/SQL-Query-Examples)

***
When using METATRYP v. 2.0 please cite the following:    
[Saunders, J. K., Gaylord, D., Held, N., Symmonds, N., et al., METATRYP v 2.0: Metaproteomic Least Common Ancestor Analysis for Taxonomic Inference Using Specialized Sequence Assemblies - Standalone Software and Web Servers for Marine Microorganisms and Coronaviruses. bioRxiv 2020, 2020.2005.2020.107490.](https://www.biorxiv.org/content/10.1101/2020.05.20.107490v1)
