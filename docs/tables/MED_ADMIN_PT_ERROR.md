# MED_ADMIN_PT_ERROR

> Medication Administration - Patient Error Table

**Description:** Medication Administration - Patient Error  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BAR_CODE_IDENT` | VARCHAR(50) | NOT NULL |  | The identifier that was scanned. |
| 2 | `EXPECTED_PT_ID` | DOUBLE | NOT NULL | FK→ | The id of the patient that was expected to be identified. |
| 3 | `FREETEXT_REASON` | VARCHAR(255) |  |  | The free text reason given for an event which the patient error event is associated. |
| 4 | `IDENTIFIED_PT_ID` | DOUBLE | NOT NULL | FK→ | The id of the patient that was identified. |
| 5 | `MED_ADMIN_ALERT_ID` | DOUBLE | NOT NULL | FK→ | ID of a medication admin alert. The foreign key to the med_admin_alert table. |
| 6 | `MED_ADMIN_PT_ERROR_ID` | DOUBLE | NOT NULL |  | The id of the patient error event. |
| 7 | `REASON_CD` | DOUBLE | NOT NULL |  | The reason selected for an event which the patient error event is associated. This column may hold reasons from multiple code sets. Alert Type to Code Set relationships: PPIDOVER/4003287. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECTED_PT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `IDENTIFIED_PT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `MED_ADMIN_ALERT_ID` | [MED_ADMIN_ALERT](MED_ADMIN_ALERT.md) | `MED_ADMIN_ALERT_ID` |

