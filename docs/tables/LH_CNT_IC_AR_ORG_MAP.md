# LH_CNT_IC_AR_ORG_MAP

> Stores the records of organisms mapping to antimicrobial agents for the purpose of NHSN reporting

**Description:** Lh_Cnt_Ic_Ar_Org_Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANTIMICROBIAL_NAME` | VARCHAR(200) | NOT NULL |  | The Antimicrobial agent which is used as an extension on codeset 1011 to identify the Antibiotics for AR reporting. This column is loaded from a csv and the client cannot update it so there is no need for the corresponding _KEY column. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. This column will store the begin effective date of antibiotic. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. This column will store the end effective date of antibiotic. |
| 5 | `LH_CNT_IC_AR_ORG_MAP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_AR_ORG_MAP table. |
| 6 | `NHSN_ORGANISM_SNOMED` | VARCHAR(100) | NOT NULL |  | The organism snomed code to use for AR organism reporting to NHSN. |
| 7 | `ORGANISM_NAME` | VARCHAR(200) | NOT NULL |  | The Organism name which is used as an extension on codeset 1021 to identify the Organisms for AR reporting. |
| 8 | `ORGANISM_NAME_KEY` | VARCHAR(200) | NOT NULL |  | Stores corresponding string values from column ORGANISM_NAME for searching in UPPER case, less SPACES or special characters. |
| 9 | `ORGANISM_NAME_KEY_A_NLS` | VARCHAR(800) | NOT NULL |  | Stores the corresponding non-english ACCENTED character set values from column ORGANISM_NAME_KEY for international searches. Database triggers handle the population of these columns so scripts and applications can ignore them. |
| 10 | `RXNORM_IDENT` | VARCHAR(60) | NOT NULL |  | Identifier from RxNorm terminology. |
| 11 | `SPECIMEN_NAME` | VARCHAR(100) | NOT NULL |  | The name of the Specimen type for AR reporting. |
| 12 | `SPECIMEN_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Stores corresponding string values from column SPECIMAN_NAME for searching in UPPER case, less SPACES or special characters. |
| 13 | `SPECIMEN_NAME_KEY_A_NLS` | VARCHAR(400) | NOT NULL |  | Stores the corresponding non-english ACCENTED character set values from column SPECIMEN_NAME_KEY for international searches. Database triggers handle the population of these columns so scripts and applications can ignore them. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

