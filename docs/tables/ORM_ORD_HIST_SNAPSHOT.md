# ORM_ORD_HIST_SNAPSHOT

> This table will be a list of medication history snapshots. These snapshots will allow the user to see how the medication history has changed.

**Description:** orm_order_history_snapshot  
**Table type:** ACTIVITY  
**Primary key:** `ORM_ORD_HIST_SNAPSHOT_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter for which the medication history snapshot was taken |
| 2 | `MED_HISTORY_STATUS_IND` | DOUBLE | NOT NULL |  | The medication history status at the time that the snapshot was taken |
| 3 | `ORM_ORD_HIST_SNAPSHOT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the orm_ord_hist_snapshot table. |
| 4 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | The person for whom the medication history snapshot was taken. |
| 5 | `PERFORMED_DT_TM` | DATETIME | NOT NULL |  | The date/time the snapshot was taken. |
| 6 | `PERFORMED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person who triggered the snapshot. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERFORMED_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ORM_ORD_HIST_SNAPSHOT_COMP](ORM_ORD_HIST_SNAPSHOT_COMP.md) | `SNAPSHOT_ID` |

