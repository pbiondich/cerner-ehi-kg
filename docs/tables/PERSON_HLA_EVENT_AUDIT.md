# PERSON_HLA_EVENT_AUDIT

> Provides an audit trail of the Person HLA Event table whenever a record is modified.

**Description:** Person HLA Event Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_DT_TM` | DATETIME |  |  | Date and time that the audit record was created. |
| 2 | `HLA_EVENT_AUDIT_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies an HLA Event History audit record. |
| 3 | `HLA_EVENT_DT_TM` | DATETIME |  |  | Date and time that the original person_hla_event record was created. |
| 4 | `HLA_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Relates this audit record to the current HLA Event History record. It is a foreign key reference to the primary key of the person_hla_event table. |
| 5 | `HLA_EVENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where HLA Event history audit trail event text is located. It is a foreign key reference to the primary key of the long_text table. |
| 6 | `HLA_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of HLA event for this record |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who updated the person_hla_event record which resulted in the creation of this audit record. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HLA_EVENT_ID` | [PERSON_HLA_EVENT](PERSON_HLA_EVENT.md) | `HLA_EVENT_ID` |
| `HLA_EVENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

