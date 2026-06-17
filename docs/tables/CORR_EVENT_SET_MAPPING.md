# CORR_EVENT_SET_MAPPING

> This table is used to map event_Sets to other event_sets. Each mapping will be associated with a correspondence_type_cd

**Description:** Correspondence Event Set Mapping  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CORRESPONDENCE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of correspondence this mapping is valid for. |
| 2 | `CORR_EVENT_SET_MAPPING_ID` | DOUBLE | NOT NULL |  | Unique identifier for mapping row. |
| 3 | `EVENT_SET_NAME` | VARCHAR(255) | NOT NULL |  | The from event set name.Column |
| 4 | `INHERITANCE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the event set mapping supersedes or adds to previous event set mappings higher in the event set hierarchy. (0 indicates the mapping combines with inherited mappings, while 1 indicates that inherited mappings are discarded). |
| 5 | `MAPPED_EVENT_SET_NAME` | VARCHAR(255) | NOT NULL |  | The event set that the from event set is mapped to |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

