# NOTE_TYPE

> List of all valid note types for the Clinical Document Tab in PowerChart

**Description:** NOTE TYPE  
**Table type:** REFERENCE  
**Primary key:** `NOTE_TYPE_ID`  
**Columns:** 15  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BANNER_IND` | DOUBLE |  |  | Banner Indicator. |
| 2 | `DATA_STATUS_IND` | DOUBLE |  |  | 1 if the note type is active 0 otherwise |
| 3 | `DEFAULT_LEVEL_FLAG` | DOUBLE | NOT NULL |  | Specifies the default level for documents generated with this note type. |
| 4 | `DEFAULT_SERVICE_DATE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 5 | `DEVICE_NAME` | VARCHAR(100) |  |  | printer name |
| 6 | `EVENT_CD` | DOUBLE | NOT NULL |  | event code that corresponds to the note type. |
| 7 | `NOTE_TYPE_DESCRIPTION` | VARCHAR(50) |  |  | description of the note type. Initially matches the event_cd display |
| 8 | `NOTE_TYPE_ID` | DOUBLE | NOT NULL | PK | unique primary key for the table. |
| 9 | `OVERRIDE_LEVEL_IND` | DOUBLE | NOT NULL |  | Indicates if the user can override the default level specified by DEFAULT_LEVEL_FLAG. The default is 1 which means it can be overridden. |
| 10 | `PUBLISH_LEVEL` | DOUBLE |  |  | 0-default(AUTH = 5) 1-InProgress 2-Transcribe 3-UnAuth 4-Auth 5-Modify |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [INVTN_PROGRAM_GROUP](INVTN_PROGRAM_GROUP.md) | `NOTE_TYPE_ID` |
| [MSG_DOC_FAVORITES](MSG_DOC_FAVORITES.md) | `NOTE_ID` |
| [NOTE_TYPE_LIST](NOTE_TYPE_LIST.md) | `NOTE_TYPE_ID` |
| [NOTE_TYPE_SCR_PATTERN_RELTN](NOTE_TYPE_SCR_PATTERN_RELTN.md) | `NOTE_TYPE_ID` |
| [NOTE_TYPE_TEMPLATE_RELTN](NOTE_TYPE_TEMPLATE_RELTN.md) | `NOTE_TYPE_ID` |
| [PDOC_NOTE_TYPE_PREF_R](PDOC_NOTE_TYPE_PREF_R.md) | `NOTE_TYPE_ID` |

