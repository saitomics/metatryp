# METATRYP v. 1.1 Documentation
These tools are intended to help researchers answer questions about proteomics data. Written in Python 2.7 and implemented on a Unix operating system (linux/macOS).

The METATRYP software consists of:
1. a database, stored in a standalone SQLite file.
2. python libraries, for processing, ingesting, and analyzing data. 
3. command-line scripts, to act as interfaces to the python libraries and the database.

***

* [Overview](https://github.com/saitomics/metatryp/wiki/Overview)
* [Installation Instructions](https://github.com/saitomics/metatryp/wiki/Installation-Instructions)
    * [Download](https://github.com/saitomics/metatryp/wiki/Installation-Instructions#1-download-this-repository-follow-a-or-b)
    * [Create virtual environment](https://github.com/saitomics/metatryp/wiki/Installation-Instructions#2-create-a-virtual-environment-follow-a-or-b)
    * [Run tests](https://github.com/saitomics/metatryp/wiki/Installation-Instructions#3-run-tests)
    * [Initialize database](https://github.com/saitomics/metatryp/wiki/Installation-Instructions#4-initialize-the-sqlite-database-follow-a-or-b)
* [Quick Usage Guide](https://github.com/saitomics/metatryp/wiki/Quick-Usage-Guide)
    * [Digest and ingest new taxa](https://github.com/saitomics/metatryp/wiki/Quick-Usage-Guide#1-digest-and-ingest-data)
    * [Generate peptide redundancy tables](https://github.com/saitomics/metatryp/wiki/Quick-Usage-Guide#2-generate-redundancy-tables)
    * [Remove taxa from database](https://github.com/saitomics/metatryp/wiki/Quick-Usage-Guide#3-remove-taxa-from-the-database)
* [Tutorial](https://github.com/saitomics/metatryp/wiki/Tutorial)
    * [Taxa in Example Database](https://github.com/saitomics/metatryp/wiki/Tutorial/_edit#taxa-in-database)
* [Database Schema](https://github.com/saitomics/metatryp/wiki/Database-Schema)
* [Directly query database via SQL](https://github.com/saitomics/metatryp/wiki/SQL-Query-Examples)

***

For higher volume instance of the METATRYP software with additional features (like Lowest Common Ancestor Analysis), please see **METATRYP v. 2**([https://github.com/WHOIGit/metatryp-2.0](https://github.com/WHOIGit/metatryp-2.0)). A web portal using a marine microbe database can be found at [https://metatryp.whoi.edu/](https://metatryp.whoi.edu/), and a portal using a coronavirus focused database can be found at [https://metatryp-coronavirus.whoi.edu/](https://metatryp-coronavirus.whoi.edu/).

When using METATRYP v. 1 please cite the following:    
[Saito, M.A., Dorsk, A., Post, A.F., McIlvin, M.R., Rappé, M.S., DiTullio, G.R. and Moran, D.M. (2015), Needles in the blue sea: Sub‐species specificity in targeted protein biomarker analyses within the vast oceanic microbial metaproteome. Proteomics, 15: 3521-3531. doi:10.1002/pmic.201400630](https://onlinelibrary.wiley.com/doi/full/10.1002/pmic.201400630)
