# CV_FAILED_TRAN_BLOB

> To store the XML or PDF data saved as Media Object during the Transaction failure.

**Description:** Transaction BLOB table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_TYPE_TFLG` | VARCHAR(20) |  |  | This is a Text Flag field which indicates if the BLOB field contains PDF or XML data stored as a Media Object. during the transaction failure. AKA "Stream_Handle." Valid values are PDF or XML |
| 2 | `CV_FAILED_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | A Foreign Key value which identifies the Failed Transaction in the CV_FAILED_TRANSACTION table. |
| 3 | `CV_FAILED_TRAN_BLOB_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `FAILED_TRAN_BLOB` | LONGBLOB |  |  | A BLOB field which contains the PDF or XML data Media Object related to the fail |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_FAILED_TRANSACTION_ID` | [CV_FAILED_TRANSACTION](CV_FAILED_TRANSACTION.md) | `CV_FAILED_TRANSACTION_ID` |

