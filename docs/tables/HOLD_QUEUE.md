# HOLD_QUEUE

> This table references ESO events that are held from going outbound from HNAM. Entries on this table directly reference the outbound events on the CQM_FSIESO_QUE table. Entries are deleted from this table in run time, as hold release conditions are met.

**Description:** Hold Queue  
**Table type:** ACTIVITY  
**Primary key:** `HOLD_QUEUE_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_COMBINE_IND` | DOUBLE |  |  | This element will be set to 1 when the that the encntr_id was combined and communication to the FSI Hold Release failed. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 3 | `HOLD_QUEUE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the hold_queue table. It is an internal system assigned number. |
| 4 | `HOLD_RULE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the hold_rule table. It is an internal system assigned number. |
| 5 | `LGTMT_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the LEGITIMATE_RELATIONSHIP table. It is an internal system assigned number. This column is obsolete because the parent table, LEGITIMATE RELATIONSHIP is obsolete. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the orders table. It is an internal system assigned number. |
| 7 | `PERSON_COMBINE_IND` | DOUBLE |  |  | This element will be set to 1 when the that the person_id was combined and communication to the FSI Hold Release failed. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 9 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the cqm_fsieso_que table. It is an internal system assigned number. |
| 10 | `SCH_EVENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 11 | `TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CQM listener trigger table (CQM_FSIESO_TR_1). It is an internal system assigned number. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HOLD_RULE_ID` | [HOLD_RULE](HOLD_RULE.md) | `HOLD_RULE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `QUEUE_ID` | [CQM_FSIESO_QUE](CQM_FSIESO_QUE.md) | `QUEUE_ID` |
| `TRIGGER_ID` | [CQM_FSIESO_TR_1](CQM_FSIESO_TR_1.md) | `TRIGGER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HOLD_QUEUE_CONDITION](HOLD_QUEUE_CONDITION.md) | `HOLD_QUEUE_ID` |

