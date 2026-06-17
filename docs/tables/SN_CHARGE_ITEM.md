# SN_CHARGE_ITEM

> SurgiNet Charge Item Table

**Description:** SurgiNet Charge Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | The Unique Identifier on the Table |
| 7 | `CHARGE_TYPE_FLAG` | DOUBLE |  |  | Charge Type Flag |
| 8 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The Application Context creating the row |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | The Date and Time the Row was createdColumn |
| 10 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The Personnel respnosible for creating this row. |
| 11 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The task that was used in creating the row |
| 12 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document Type Code for which this charge is being sent |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_ID` | DOUBLE | NOT NULL |  | The Id that references to the Event Id on the AFC request |
| 15 | `EVENT_NAME` | VARCHAR(30) |  |  | The Table name that contains the Event ID can be Item_Master, Order_Catalog or Surgical_Case |
| 16 | `IN_PROCESS_IND` | DOUBLE |  |  | Indicates if the charge is in the process of being sent. |
| 17 | `QUANTITY` | DOUBLE | NOT NULL |  | This is the quantity which has been charged |
| 18 | `REFERENCE_ID` | DOUBLE | NOT NULL |  | Reference_Id in the AFC Request |
| 19 | `REFERENCE_NAME` | VARCHAR(30) |  |  | The Table name that contains the Reference ID can be Surg_Case_Procedure, Case_Cart_Pick_List, Code_Value |
| 20 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | The Surgical Case Id this charge item is for. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

