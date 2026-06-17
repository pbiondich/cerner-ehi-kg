# UKRWH_CDE_CODE_VALUE

> Contains Code Values along with corresponding NHS Reporting outbound aliases.

**Description:** UK Reporting Warehouse Consolidated Data Extract Code Value  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_SET` | VARCHAR(40) |  |  | The code set for the code value |
| 2 | `CODE_VALUE` | VARCHAR(40) |  |  | Stores the actual code values for a given numeric code_set |
| 3 | `CODE_VALUE_ACTIVE_IND` | DOUBLE |  |  | The Millennium code value table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `CODE_VALUE_SET_DISPLAY` | VARCHAR(40) |  |  | Display of the code set |
| 5 | `DEFINITION` | VARCHAR(100) |  |  | The display string for the code_value |
| 6 | `DESCRIPTION` | VARCHAR(60) |  |  | The description for the code value |
| 7 | `DISPLAY` | VARCHAR(40) |  |  | The display string for the code_value |
| 8 | `DISPLAY_UNF` | VARCHAR(40) |  |  | Same as display only converted to upper case |
| 9 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 11 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 14 | `NHSREPORT_CV_OUTBOUND_ALIAS` | VARCHAR(100) |  |  | This field contains the code value for the NHS Report Outbound alias |
| 15 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 16 | `UKRWH_CDE_CODE_VALUE_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde code value table. It is an internal system assigned number. |
| 17 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

