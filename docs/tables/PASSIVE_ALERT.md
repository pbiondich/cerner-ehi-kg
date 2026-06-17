# PASSIVE_ALERT

> Each row on the table represents a passive alert to be displayed in patient chart.

**Description:** PASSIVE ALERT  
**Table type:** ACTIVITY  
**Primary key:** `PASSIVE_ALERT_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PARAM_TXT` | VARCHAR(255) | NOT NULL |  | Action parameter for the alert based on the action. For LAUNCHFORM action, set the dcp_forms_id to launch the PowerForm. For NAVIGATE action, set the component name to navigate to . For LAUNCHURL action, set the url to open the browser. |
| 2 | `ACTION_TYPE_TXT` | VARCHAR(30) | NOT NULL |  | Action type for the alert such as launching PowerForms - LAUNCHFORM, smart navigating to table of content within PowerChart - SMARTNAV, launching browser - LAUNCH. This is intended for simple next step with limited information. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ALERT_REMOVAL_SOURCE` | VARCHAR(30) |  |  | Provides the name of the EKS module that was used to inactivate the alert. |
| 5 | `ALERT_SOURCE` | VARCHAR(30) |  |  | Provides the name of the EKS module that was used to add the alert to the table. |
| 6 | `ALERT_TXT` | VARCHAR(255) | NOT NULL |  | Alert Message |
| 7 | `ALLOW_DISMISS_IND` | DOUBLE | NOT NULL |  | Indicator to signify dismiss action allowed on the passive alert |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CATEGORY_CD` | DOUBLE | NOT NULL | FK→ | The Alert Category |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `PASSIVE_ALERT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY. Value of the unique primary identifier of the table. It is an internal system assigned number. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATEGORY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PASSIVE_ALERT_ACTION](PASSIVE_ALERT_ACTION.md) | `PASSIVE_ALERT_ID` |
| [PASSIVE_ALERT_POSITION](PASSIVE_ALERT_POSITION.md) | `PASSIVE_ALERT_ID` |

