# SA_MACRO

> Contains records that document when macros are run for a particular anesthesia record Based on how many macros they execute in a case. Estimate 4:1 with SA_ANESTHESIA_RECORD. 104,400

**Description:** SA Macro  
**Table type:** ACTIVITY  
**Primary key:** `SA_MACRO_ID`  
**Columns:** 14  
**Referenced by:** 15 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `EXECUTE_DT_TM` | DATETIME |  |  | The date/time the macro was executed |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user that executed the macro |
| 7 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The anesthesia record that this macro was executed for |
| 8 | `SA_MACRO_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the macro record |
| 9 | `SA_REF_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The reference macro that this execution was based on |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |
| `SA_REF_MACRO_ID` | [SA_REF_MACRO](SA_REF_MACRO.md) | `SA_REF_MACRO_ID` |

## Referenced by (15)

| From table | Column |
|------------|--------|
| [SA_ACTION](SA_ACTION.md) | `SA_MACRO_ID` |
| [SA_ACTION_ITEM](SA_ACTION_ITEM.md) | `SA_MACRO_ID` |
| [SA_FLUID](SA_FLUID.md) | `SA_MACRO_ID` |
| [SA_FLUID_ADMIN](SA_FLUID_ADMIN.md) | `SA_MACRO_ID` |
| [SA_ITEM](SA_ITEM.md) | `SA_MACRO_ID` |
| [SA_ITEM_USAGE](SA_ITEM_USAGE.md) | `SA_MACRO_ID` |
| [SA_MEDICATION](SA_MEDICATION.md) | `SA_MACRO_ID` |
| [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `SA_MACRO_ID` |
| [SA_PARAMETER](SA_PARAMETER.md) | `SA_MACRO_ID` |
| [SA_PARAMETER_MONITOR](SA_PARAMETER_MONITOR.md) | `SA_MACRO_ID` |
| [SA_TODO_ACTION](SA_TODO_ACTION.md) | `SA_MACRO_ID` |
| [SA_TODO_FLUID](SA_TODO_FLUID.md) | `SA_MACRO_ID` |
| [SA_TODO_ITEM](SA_TODO_ITEM.md) | `SA_MACRO_ID` |
| [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `SA_MACRO_ID` |
| [SA_TODO_PARAMETER](SA_TODO_PARAMETER.md) | `SA_MACRO_ID` |

