# PULSE_GEN_SESSION

> Contains information about a device interrogation session

**Description:** Pulse Generator Session  
**Table type:** ACTIVITY  
**Primary key:** `PULSE_GEN_SESSION_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICIAN_CONTACT` | VARCHAR(100) |  |  | The contact information for the responsible clinician |
| 2 | `CLINICIAN_NAME` | VARCHAR(50) |  |  | The name of the clinician that is responsible for the examination |
| 3 | `CLINIC_NAME` | VARCHAR(50) |  |  | The name of the clinic where the examination took place |
| 4 | `PULSE_GEN_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator associated with this interrogation session |
| 5 | `PULSE_GEN_SESSION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `REPROGRAMMED_CD` | DOUBLE | NOT NULL |  | The indication of whether the device was reprogrammed during the session |
| 7 | `SESSION_DT_TM` | DATETIME |  |  | The date and time of the in-clinic or remote interrogation session |
| 8 | `TYPE_CD` | DOUBLE | NOT NULL |  | The type of device interaction that generated the current data set |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_ID` | [PULSE_GEN](PULSE_GEN.md) | `PULSE_GEN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PULSE_GEN_SESSION_DOC](PULSE_GEN_SESSION_DOC.md) | `PULSE_GEN_SESSION_ID` |

