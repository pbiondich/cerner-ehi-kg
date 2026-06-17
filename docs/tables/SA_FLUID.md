# SA_FLUID

> Contains records that document what fluids are used in an anesthesia record Based on the number of fluids used during a case. Estimate 5:1 with SA_ANESTHESIA_RECORD. 130,500

**Description:** SA Fluids  
**Table type:** ACTIVITY  
**Primary key:** `SA_FLUID_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DISPLAY_SEQ` | DOUBLE |  |  | used to see records based on sequence and also can resequence the records when ever needed |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User that added the fluid to the anesthesia record, if 0, added by macro |
| 7 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The anesthesia record that this fluid is being documented on |
| 8 | `SA_FLUID_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the fluid record |
| 9 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | Ties to the macro that added the fluid to the anesthesia record, if 0, done by user |
| 10 | `SA_REF_FLUID_ID` | DOUBLE | NOT NULL | FK→ | Ties to the SA_REF_FLUID table to identify the fluid that was added |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_REF_FLUID_ID` | [SA_REF_FLUID](SA_REF_FLUID.md) | `SA_REF_FLUID_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_FLUID_ADMIN](SA_FLUID_ADMIN.md) | `SA_FLUID_ID` |

