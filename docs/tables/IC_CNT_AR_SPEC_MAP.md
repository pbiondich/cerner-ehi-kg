# IC_CNT_AR_SPEC_MAP

> This table will contain a list of organism-drug-specimen type mappings for AR reporting.

**Description:** Infection Control Content AR Specimen Mapping  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONCEPT_IDENT` | DOUBLE |  |  | This column will store the concept id of specimen. Corresponds to Concept_ID in NHSN terminology. Note! This column has been made obsolete. It was decided we needed a Varchar2 column to store this data. |
| 3 | `CONCEPT_IDENT_TXT` | VARCHAR(60) |  |  | This column will store the concept id of specimen. Corresponds to Concept_ID in NHSN terminology. This column replaces column CONCEPT_IDENT. It was determined we needed the data stored in a varchar2 data type column. |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | The date/time when the specimen was created in the table. |
| 5 | `IC_CNT_AR_SPEC_MAP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the IC_CNT_AR_SPEC_MAP table. |
| 6 | `SPECIMEN_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | This column will store begin effective date of specimen. |
| 7 | `SPECIMEN_CATEGORY_NAME` | VARCHAR(250) |  |  | This column will store the category of specimen type(for all blood related it will hold blood and urine related it will hold Urine, etc). |
| 8 | `SPECIMEN_END_EFFECTIVE_DT_TM` | DATETIME |  |  | This column will store end effective date of specimen. |
| 9 | `SPECIMEN_NAME` | VARCHAR(250) |  |  | This column will store the name of the specimen. |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

