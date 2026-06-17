# RAD_PROCEDURE_ASSOC

> The Rad_Procedure_Assoc table contain the procedures that exist within a procedure grouping.

**Description:** Rad Procedure Associations  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSESSMENT_RECOMMENDATION_FLAG` | DOUBLE | NOT NULL |  | Indicates if Assessment is Required(1), Optional(2) or Not Allowed (3) |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The Catalog_Cd is a foreign key to the Order_Catalog table. This identifies the procedure is a part of the procedure group. |
| 3 | `EXCLUDE_FROM_AUDIT_FLAG` | DOUBLE | NOT NULL |  | Indicates if cases containing this procedure should be Excluded(1) from or Included(2) in audit calculations |
| 4 | `INDICATION_FOR_EXAM_ID` | DOUBLE | NOT NULL | FK→ | Reason the exam is required for this procedure. |
| 5 | `MANAGEMENT_FLAG` | DOUBLE | NOT NULL |  | Indicates if a recommendation is Required(1), Optional(2) or Not Allowed (3) |
| 6 | `NOTIFICATION_LETTER_FLAG` | DOUBLE | NOT NULL |  | Indicates if Notification Letter is Required(1) or Optional(2) |
| 7 | `NO_FOLLOW_UP_FLAG` | DOUBLE | NOT NULL |  | Indicates if No Follow-up is Required(1), Optional(2) or Not Allowed (3). |
| 8 | `PROC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The Proc_Group_Id is a foreign key to the Rad_Procedure_Assoc table. This uniquely identifies the procedure group. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `INDICATION_FOR_EXAM_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `PROC_GROUP_ID` | [RAD_PROCEDURE_GROUP](RAD_PROCEDURE_GROUP.md) | `PROC_GROUP_ID` |

