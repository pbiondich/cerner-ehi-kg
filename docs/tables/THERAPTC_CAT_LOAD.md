# THERAPTC_CAT_LOAD

> Load table for taking 3rd party content and uploading to THERAPEUTIC_CAT table. Community tables we truncate and reload in house, and ship to clients, to load 3rd party content without downtime.

**Description:** THERAPEUTIC CAT LOAD  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_NAME` | VARCHAR(255) | NOT NULL |  | Source string from nomenclature table |
| 2 | `EXTERNAL_IDENT` | VARCHAR(255) | NOT NULL |  | Primary Key column. |
| 3 | `SOURCE_VOCAB_MEAN` | VARCHAR(12) | NOT NULL |  | CDF Meaning of Source Vocabulary. To be able to use these tables for other terminologies besides SNOMED in the future |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

