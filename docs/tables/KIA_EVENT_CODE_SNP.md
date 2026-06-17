# KIA_EVENT_CODE_SNP

> Event Code snapshot

**Description:** KIA EVENT CODE SNP  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_STATUS_CD` | DOUBLE | NOT NULL |  | describes the event code status.Column |
| 2 | `COLLATING_SEQ` | DOUBLE | NOT NULL |  | defines an ordering of sections within an mdoc..Column |
| 3 | `DEF_DOCMNT_ATTRIBUTES` | VARCHAR(255) |  |  | describes the attributes of the default document.Column |
| 4 | `DEF_DOCMNT_FORMAT_CD` | DOUBLE | NOT NULL |  | code for the default document format.Column |
| 5 | `DEF_DOCMNT_STORAGE_CD` | DOUBLE | NOT NULL |  | code for the default document storage.Column |
| 6 | `DEF_EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | code for the default event class.Column |
| 7 | `DEF_EVENT_CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | code for the default event confidence level.Column |
| 8 | `DEF_EVENT_LEVEL` | DOUBLE |  |  | the default value for the view_level field in the clinical_event table if one is not specified in the ensure. the view level controls the viewability of a clinical_event row in the flowsheet, where a value of 0 would not be viewable, 1 would be viewable at the lowest granularity of time, and 9 would be viewable at the highest granularity of time. |
| 9 | `EVENT_ADD_ACCESS_IND` | DOUBLE |  |  | flag to indicate if events of this type can be added by powerchart.Column |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL | FK→ | it is the code that identifies the most basic unit of storage.Column |
| 11 | `EVENT_CD_DEFINITION` | VARCHAR(100) |  |  | definition of the event code.Column |
| 12 | `EVENT_CD_DESCR` | VARCHAR(60) |  |  | description of the event code.Column |
| 13 | `EVENT_CD_DISP` | VARCHAR(40) |  |  | event code display name key.Column |
| 14 | `EVENT_CD_DISP_KEY` | VARCHAR(40) |  |  | defines the key to the event code display name.Column |
| 15 | `EVENT_CHG_ACCESS_IND` | DOUBLE |  |  | flag to indicate events of this type can be changed by powerchart.Column |
| 16 | `EVENT_CODE_STATUS_CD` | DOUBLE | NOT NULL |  | code for the event code status.Column |
| 17 | `EVENT_SET_NAME` | VARCHAR(40) |  |  | a foreign key to the v500_event_set_code table to define hierarchy, display rules, calculation rules, etc. |
| 18 | `RETENTION_DAYS` | DOUBLE |  |  | number of days events with this event code should exist before being purged.Column |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

