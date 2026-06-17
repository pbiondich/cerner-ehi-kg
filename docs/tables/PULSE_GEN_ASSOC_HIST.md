# PULSE_GEN_ASSOC_HIST

> Contains information regarding the association and removal of association of a pulse generator

**Description:** Pulse Generator Association History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSOCIATION_DT_TM` | DATETIME |  |  | The date and time the pulse generator was associated to a person |
| 2 | `ASSOC_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who associated this device |
| 3 | `DISASSOCIATION_DT_TM` | DATETIME |  |  | The date and time the association of the pulse generator was removed. |
| 4 | `DISASSOC_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who disassociated this device |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The Person associated with this history item |
| 6 | `PULSE_GEN_ASSOC_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `PULSE_GEN_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator associated with this history item |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSOC_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DISASSOC_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PULSE_GEN_ID` | [PULSE_GEN](PULSE_GEN.md) | `PULSE_GEN_ID` |

