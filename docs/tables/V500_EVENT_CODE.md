# V500_EVENT_CODE

> Reference table storing clincial event codes. One to one mapping with code set 72.

**Description:** Reference table storing clincial event codes.  
**Table type:** REFERENCE  
**Primary key:** `EVENT_CD`  
**Columns:** 24  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_STATUS_CD` | DOUBLE | NOT NULL |  | Describes the event code status. |
| 2 | `COLLATING_SEQ` | DOUBLE | NOT NULL |  | Defines an ordering of sections within an MDOC. |
| 3 | `DEF_DOCMNT_ATTRIBUTES` | VARCHAR(255) |  |  | Describes the attributes of the default document. |
| 4 | `DEF_DOCMNT_FORMAT_CD` | DOUBLE | NOT NULL |  | Code for the default document format. |
| 5 | `DEF_DOCMNT_STORAGE_CD` | DOUBLE | NOT NULL |  | Code for the default document storage. |
| 6 | `DEF_EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | Code for the default event class. |
| 7 | `DEF_EVENT_CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | Code for the default event confidence level. |
| 8 | `DEF_EVENT_LEVEL` | DOUBLE |  |  | The default value for the view_level field in the clinical_event table if one is not specified in the ensure. The view level controls the viewability of a clinical_event row in the flowsheet, where a value of 0 would not be viewable, 1 would be viewable at the lowest granularity of time, and 9 would be viewable at the highest granularity of time. |
| 9 | `EVENT_ADD_ACCESS_IND` | DOUBLE |  |  | Flag to indicate if events of this type can be added by PowerChart. |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL | PK | It is the code that identifies the most basic unit of storage. |
| 11 | `EVENT_CD_DEFINITION` | VARCHAR(100) |  |  | Definition of the event code. |
| 12 | `EVENT_CD_DESCR` | VARCHAR(60) |  |  | Description of the event code. |
| 13 | `EVENT_CD_DISP` | VARCHAR(40) |  |  | Event code display name key. |
| 14 | `EVENT_CD_DISP_KEY` | VARCHAR(40) |  |  | Defines the key to the event code display name. |
| 15 | `EVENT_CD_SUBCLASS_CD` | DOUBLE | NOT NULL |  | Obsolete field |
| 16 | `EVENT_CHG_ACCESS_IND` | DOUBLE |  |  | Flag to indicate of events of this type can be changed by PowerChart. |
| 17 | `EVENT_CODE_STATUS_CD` | DOUBLE | NOT NULL |  | Code for the event code status. |
| 18 | `EVENT_SET_NAME` | VARCHAR(40) |  |  | A foreign key to the v500_event_set_code table to define hierarchy, display rules, calculation rules, etc. |
| 19 | `RETENTION_DAYS` | DOUBLE |  |  | Number of days events with this event code should exist before being purged. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `EVENT_CD` |
| [OUTCOME_CATALOG](OUTCOME_CATALOG.md) | `EVENT_CD` |
| [V500_EVENT_SET_EXPLODE](V500_EVENT_SET_EXPLODE.md) | `EVENT_CD` |

