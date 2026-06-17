# RAD_LOAN_INFO

> The Rad_Loan_Info table contains information about an image management loan transaction.

**Description:** Rad Loan Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGENT` | VARCHAR(50) |  |  | The Agent identifies the person who picked up the films/folders for the person/place that borrowed it. |
| 2 | `COMMENTS` | VARCHAR(255) |  |  | The Comments field contains any general comments about the loan. |
| 3 | `DUE_DT_TM` | DATETIME |  |  | The Due_Dt_Tm contains the date that the loan is due to be returned. |
| 4 | `LOAN_TYPE_FLAG` | DOUBLE |  |  | The Loan_Type_Flag identifies whether the films/folders were loaned to a physician, patient, internal location, or an external borrower. |
| 5 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Trackable_Object table. It identifies the folder/film that is on loan. |
| 6 | `TRACKING_POINT_CD` | DOUBLE | NOT NULL |  | The Tracking_Point_Cd identifies the borrower. Which table this field a foreign key to is determined by the Loan_Type_Flag. |
| 7 | `TRANS_METHOD_CD` | DOUBLE | NOT NULL |  | the Trans_Method_Cd identifies the method that the loan was sent. (ex. agent, courier, mail, etc.) |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQ_OBJECT_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |

