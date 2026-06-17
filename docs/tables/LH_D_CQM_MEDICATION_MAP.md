# LH_D_CQM_MEDICATION_MAP

> This table is used to store reference data based off of the Clinical Quality Measures Bedrock and Multum components

**Description:** LH_D_CQM_MEDICATION_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The Begin effective date/time for the mapping |
| 2 | `CATEGORY_MEAN` | VARCHAR(100) |  |  | Unique string for a category |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The End effective date/time for the mapping |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 6 | `LH_D_CQM_MEDICATION_MAP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_CQM_MEDICATION_MAP table. |
| 7 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 8 | `SOURCE_VOCAB_ITEM_IDENT` | VARCHAR(50) |  |  | The identifier that the Millennium value is mapped to |
| 9 | `SOURCE_VOCAB_MEAN` | VARCHAR(50) |  |  | The type of identifier as identified by CMS |
| 10 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | A Millennium synonym that identifies the medication |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record |
| 14 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALUE_SET_NAME` | VARCHAR(255) |  |  | The CMS Value Set Name |
| 16 | `VOCAB_OID_TXT` | VARCHAR(100) |  |  | The CMS Value Set Identifier |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

