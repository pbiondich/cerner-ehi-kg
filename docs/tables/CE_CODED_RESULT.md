# CE_CODED_RESULT

> The ce_coded_result table contains diagnosis and other coded data.

**Description:** ce coded result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACR_CODE_STR` | VARCHAR(15) |  |  | If this is an ACR code, this field will hold the code value, and the nomenclature_id field will be null. This field will be null if this is not an ACR code. |
| 2 | `DESCRIPTOR` | VARCHAR(255) |  |  | Textual modifier of the coded result. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Event Table. |
| 4 | `GROUP_NBR` | DOUBLE |  |  | Optional grouping of coded results within the parent clinical event. |
| 5 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Foreign key to the medical nomenclature table. Will only be null for ACR codes. |
| 6 | `PATHOLOGY_STR` | VARCHAR(15) |  |  | pathology component of acr code |
| 7 | `PROC_CODE_STR` | VARCHAR(5) |  |  | proc code component of acr code |
| 8 | `RESULT_CD` | DOUBLE | NOT NULL |  | Allows the use of a code value instead of a nomenclature id. The code set of the code_value is user defined. |
| 9 | `RESULT_SET` | DOUBLE |  |  | A non-nomenclature option. Code set of result_cd if it is not null. |
| 10 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Sequence Nbr is used to make the primary key unique in the case alpha result occupies more than one row. |
| 11 | `UNIT_OF_MEASURE_CD` | DOUBLE |  |  | Unit of measure for coded results which are numeric in nature |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 18 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

