# UKRWH_CDS_NHS_DATA_DICT

> Contains Reference Descriptiions for NHS Data Dictionary Code values.

**Description:** UK Reporting Warehouse Comm Data Set National Health Service Data Dictionary  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `DATA_DICT_CODE_NHS` | VARCHAR(20) |  |  | This field contains the NHS code for the NHS Data Dictionary Data element |
| 3 | `DATA_DICT_DEFAULT_IND` | DOUBLE |  |  | This field indicates whether the particular NHS Data Dictionary Data element has a default value |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 9 | `NHS_DATA_DICT_DESCRIPTION_TXT` | VARCHAR(200) |  |  | This field contains the description for the NHS Data Dictionary Data element |
| 10 | `NHS_DATA_DICT_ELEMENT_NAME` | VARCHAR(100) |  |  | This field contains the name of the NHS Data Dictionary Data element |
| 11 | `NHS_DATA_DICT_ELEMENT_NAME_UNF` | VARCHAR(100) |  |  | This field contains the name key of the NHS Data Dictionary Data element |
| 12 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 13 | `UKRWH_CDS_NHS_DATA_DICT_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds nhs data dict table. It is an internal system assigned number. |
| 14 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

