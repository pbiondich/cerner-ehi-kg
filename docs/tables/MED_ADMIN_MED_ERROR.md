# MED_ADMIN_MED_ERROR

> Medical Administration Medication Error Table

**Description:** Medical Administration Medication Error  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | The action sequence of the order that the medication admin error event is associated to. |
| 2 | `ADMIN_DT_TM` | DATETIME |  |  | The date/time of when the administration was given. |
| 3 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | The route chosen for event that the medication admin error event is associated to. |
| 4 | `ADMIN_TZ` | DOUBLE |  |  | The time zone associated to the admin date/time. |
| 5 | `CRITICAL_DRUG_IND` | DOUBLE | NOT NULL |  | Indicates that the medication error occurred on a critically defined medication. |
| 6 | `ENCOUNTER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the encounter associated to this medication admin error event. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | The ID of the clinical event associated to this medication admin error event. |
| 8 | `FREETEXT_REASON` | VARCHAR(255) |  |  | The free text reason given for an event that the medication admin error event is associated. |
| 9 | `MED_ADMIN_ALERT_ID` | DOUBLE | NOT NULL | FK→ | ID of a medication admin alert. The foreign key to the med_admin_alert table. |
| 10 | `MED_ADMIN_MED_ERROR_ID` | DOUBLE | NOT NULL |  | The id of the medication admin error event. |
| 11 | `NEEDS_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Indicator on whether this order is verified. 0 No Verify Needed 1 Verify 40 Needed 2 Superseded 3 Verified 4 Rejected 5 Reviewed |
| 12 | `NEXT_ADMIN_DT_TM` | DATETIME |  |  | The date/time of the next scheduled administration for this event. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order associated to this medication admin error event. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person associated to this medication admin error event. |
| 15 | `PREVIOUS_ADMIN_DT_TM` | DATETIME |  |  | The date/time of the previous scheduled administration for this event. |
| 16 | `REASON_CD` | DOUBLE | NOT NULL |  | The reason selected for an event which the medication admin error event is associated. This column may hold reasons from multiple code sets. Alert Type to Code Set relationships: EARLYLATE/4000020, MEDINTALERT/4000020, MEDINTOVER/4000020, MEDSCANOVER/4003287 |
| 17 | `SCHEDULED_DT_TM` | DATETIME |  |  | The date/time of when the administration was scheduled to be given. |
| 18 | `SCHEDULED_TZ` | DOUBLE |  |  | The time zone associated to the scheduled date/time. |
| 19 | `TEMPLATE_ORDER_ID` | DOUBLE | NOT NULL |  | Order id for the template order. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `VERIFICATION_DT_TM` | DATETIME |  |  | The date and time verification of the order took place. |
| 26 | `VERIFICATION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 27 | `VERIFIED_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel that verified the order. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCOUNTER_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MED_ADMIN_ALERT_ID` | [MED_ADMIN_ALERT](MED_ADMIN_ALERT.md) | `MED_ADMIN_ALERT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

