# CNT_WV_SECTION_KEY

> Contains details about working view sections which are used by Bedrock tool. Imported using content manager tool.

**Description:** Content Working View Section Key  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_WV_SECTION_KEY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CNT_WV_SECTION_KEY table. |
| 2 | `DCP_WV_SECTION_REF_ID` | DOUBLE |  | FK→ | When the configuration is imported from from .xml/.czf to this table, ithis column will be populated with a null value. When Bedrock tool maps this record, it will be updated to the parent row from WORKING_VIEW_SECTION. |
| 3 | `DEFAULT_OPEN_PREF_FLAG` | DOUBLE | NOT NULL |  | Default open preference for the section, which is copied from preference manager's default level |
| 4 | `DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | The display name of the section |
| 5 | `EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the child event set name associated to a working view. |
| 6 | `INCLUDED_IND` | DOUBLE | NOT NULL |  | Specifies whether the event set is included on the working view. |
| 7 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Specifies whether the event set is required (for documentation and can't be removed) on the working view. |
| 8 | `SECTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of the section (0=event set; 1=IV Drip) |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | Date and time when this record was updated, used in versioning of the working view section in conjunction with UID column. |
| 15 | `WV_SECTION_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of working view section in conjunction with version_dt_tm column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_WV_SECTION_REF_ID` | [WORKING_VIEW_SECTION](WORKING_VIEW_SECTION.md) | `WORKING_VIEW_SECTION_ID` |

