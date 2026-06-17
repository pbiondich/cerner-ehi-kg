# TRACK_REFERENCE

> Reference table used to contain reference data for various tracking reference types defined in the 16409 code_set.

**Description:** Tracking Reference Table  
**Table type:** REFERENCE  
**Primary key:** `TRACKING_REF_ID`  
**Columns:** 25  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSOC_CODE_VALUE` | DOUBLE |  |  | This is the code value item that is associated with a code value element that is used by the PM application. This field will contain code values for various code sets. |
| 3 | `COMPLETE_IND` | DOUBLE |  |  | Complete Indicator used to identify if the registration status is a complete or active status. |
| 4 | `CRITICAL_BLINK_IND` | DOUBLE |  |  | Critical Blink IndicatorColumn |
| 5 | `CRITICAL_COLOR` | VARCHAR(20) |  |  | Critical ColorColumn |
| 6 | `CRITICAL_ICON` | DOUBLE |  |  | Critical IconColumn |
| 7 | `CRITICAL_INTERVAL` | DOUBLE |  |  | Critical IntervalColumn |
| 8 | `DEFAULT_IND` | DOUBLE |  |  | Default Indicator used to identify if this is the default value for the tracking group and tracking reference type code. |
| 9 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of the Tracking Reference Item. |
| 10 | `DISPLAY` | VARCHAR(20) |  |  | Display description |
| 11 | `DISPLAY_KEY` | VARCHAR(50) |  |  | Display Key generated from the Display field (All Uppercase, No Spaces or Special Characters). |
| 12 | `OVERDUE_BLINK_IND` | DOUBLE |  |  | Overdue Blink IndicatorColumn |
| 13 | `OVERDUE_COLOR` | VARCHAR(20) |  |  | Overdue ColorColumn |
| 14 | `OVERDUE_ICON` | DOUBLE |  |  | Overdue IconColumn |
| 15 | `OVERDUE_INTERVAL` | DOUBLE |  |  | Overdue IntervalColumn |
| 16 | `REF_COLOR` | VARCHAR(20) |  |  | Normal Reference Color |
| 17 | `REF_ICON` | DOUBLE |  |  | Normal Reference Icon |
| 18 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL | FK→ | Tracking Group Code used to identify which tracking group this reference is currently associated with. |
| 19 | `TRACKING_REF_ID` | DOUBLE | NOT NULL | PK | Tracking Reference Identifier |
| 20 | `TRACKING_REF_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Tracking Reference Type Code used to identify the type of tracking reference being defined. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACKING_GROUP_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_REF_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [FN_OMF_ENCNTR](FN_OMF_ENCNTR.md) | `CHECKIN_ACUITY_ID` |
| [FN_OMF_ENCNTR](FN_OMF_ENCNTR.md) | `CHECKOUT_ACUITY_ID` |
| [FN_OMF_ENCNTR](FN_OMF_ENCNTR.md) | `SPECIALTY_ID` |
| [TRACKING_CHECKIN](TRACKING_CHECKIN.md) | `ACUITY_LEVEL_ID` |
| [TRACKING_CHECKIN](TRACKING_CHECKIN.md) | `DEPART_ACUITY_LEVEL_ID` |
| [TRACKING_CHECKIN](TRACKING_CHECKIN.md) | `REGISTRATION_STATUS_ID` |
| [TRACKING_CHECKIN](TRACKING_CHECKIN.md) | `SPECIALTY_ID` |
| [TRACKING_CHECKIN](TRACKING_CHECKIN.md) | `TEAM_ID` |
| [TRACKING_LOCATOR](TRACKING_LOCATOR.md) | `TRACKING_ACUITY_LEVEL_ID` |
| [TRACKING_PRSNL](TRACKING_PRSNL.md) | `TRACKING_PRSNL_TASK_ID` |
| [TRACKING_PRSNL_REF](TRACKING_PRSNL_REF.md) | `TRACKING_REF_ID` |

