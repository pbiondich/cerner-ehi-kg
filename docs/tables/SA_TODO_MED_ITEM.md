# SA_TODO_MED_ITEM

> Surginet Anesthesia To Do Medication Item

**Description:** Surginet Anesthesia To Do Med Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_AMOUNT` | DOUBLE |  |  | The admin amount for this medication item |
| 6 | `ADMIN_DOSAGE` | DOUBLE |  |  | The admin dosage for this medication item |
| 7 | `DOSING_INFUSION_RATE` | DOUBLE |  |  | The dosing infusion rate for the medication item |
| 8 | `DURATION` | DOUBLE |  |  | The duration of this item for the medication |
| 9 | `PUMP_INFUSION_RATE` | DOUBLE |  |  | The pump infusion rate for this medication item |
| 10 | `SA_TODO_MEDICATION_ID` | DOUBLE | NOT NULL | FK→ | The ToDo list medication record this item belongs to |
| 11 | `SA_TODO_MED_ITEM_ID` | DOUBLE | NOT NULL |  | Unique Identifier for this record |
| 12 | `SEQUENCE` | DOUBLE |  |  | The sequence of this item for this medication |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `WEIGHT_BASED_DOSE` | DOUBLE |  |  | The weight based dose for this medication item |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_TODO_MEDICATION_ID` | [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `SA_TODO_MEDICATION_ID` |

