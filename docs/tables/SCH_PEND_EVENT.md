# SCH_PEND_EVENT

> Contains base appointment information about an appointment which will be created

**Description:** Scheduling pending event  
**Table type:** ACTIVITY  
**Primary key:** `SCH_PEND_EVENT_ID`  
**Columns:** 16  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPT_SYNONYM_CD` | DOUBLE | NOT NULL |  | The appointment type synonym |
| 2 | `APPT_TYPE_CD` | DOUBLE | NOT NULL |  | The appointment type |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | Date and time when the entry was created |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter identifier related to the pending event. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person identifier related to the pending event. |
| 6 | `PROTOCOL_PARENT_ID` | DOUBLE |  | FK→ | The pending event identifier of the first protocol event in the series. Zero if not part of a protocol. |
| 7 | `PROTOCOL_SEQ_NBR` | DOUBLE |  |  | The sequence within the protocol. Zero if not part of a protocol. |
| 8 | `RECUR_PARENT_ID` | DOUBLE |  | FK→ | The pending event identifier of the first event in the series. Zero if not part of a recurring series |
| 9 | `RECUR_SEQ_NBR` | DOUBLE |  |  | The sequence within the recurring series. Zero if not part of a recurring series. |
| 10 | `SCH_EVENT_ID` | DOUBLE | NOT NULL |  | The event id to be used when modifying information for an existing appointment. |
| 11 | `SCH_PEND_EVENT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SCH_PEND_EVENT table. |
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
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROTOCOL_PARENT_ID` | [SCH_PEND_EVENT](SCH_PEND_EVENT.md) | `SCH_PEND_EVENT_ID` |
| `RECUR_PARENT_ID` | [SCH_PEND_EVENT](SCH_PEND_EVENT.md) | `SCH_PEND_EVENT_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SCH_PEND_EVENT](SCH_PEND_EVENT.md) | `PROTOCOL_PARENT_ID` |
| [SCH_PEND_EVENT](SCH_PEND_EVENT.md) | `RECUR_PARENT_ID` |
| [SCH_PEND_EVENT_DETAIL](SCH_PEND_EVENT_DETAIL.md) | `SCH_PEND_EVENT_ID` |
| [SCH_PEND_LOC](SCH_PEND_LOC.md) | `SCH_PEND_EVENT_ID` |
| [SCH_PEND_ORDER](SCH_PEND_ORDER.md) | `SCH_PEND_EVENT_ID` |

