# CNT_WV_KEY

> Contains details about a working view which is used by Bedrock tool. Imported using content manager tool

**Description:** Content Working View Key  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNT_WV_KEY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CNT_WV_KEY table. |
| 3 | `CURRENT_WORKING_VIEW` | DOUBLE | NOT NULL |  | The Working View that this row was copied from. |
| 4 | `DCP_WV_REF_ID` | DOUBLE |  | FK→ | When the configuration is imported from from .xml/.czf to this table, ithis column will be populated with a null value.When bedrock tool maps this record, it will be updated to the parent row from WORKING_VIEW. |
| 5 | `DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | The display name of this working view. |
| 6 | `DISPLAY_NAME_PREF` | VARCHAR(1024) |  |  | Display name of working view preference, during export copied from Default > System > Docsettypes - hierarchy |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Specifies the location associated to a working view. |
| 8 | `LOCATION_CDUID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of location cd in conjunction with version_dt_tm column |
| 9 | `LOCATION_DISPLAY_TXT` | VARCHAR(40) | NOT NULL |  | Display text of LOCATION CD |
| 10 | `POSITION_CD` | DOUBLE | NOT NULL |  | Specifies the position associated to a working view. |
| 11 | `POSITION_CDUID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of position cd in conjunction with version_dt_tm column |
| 12 | `POSITION_DISPLAY_TXT` | VARCHAR(40) | NOT NULL |  | Display text of POSITION CD from the CODE_VALUE table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | Date and time when this record was updated |
| 19 | `VERSION_NUM` | DOUBLE | NOT NULL |  | The version number of this working view. |
| 20 | `VIEW_STATE_FLAG` | DOUBLE | NOT NULL |  | Describes the state of the view on this row. |
| 21 | `WORKING_VIEW_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of working views in conjunction with version_dt_tm column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_WV_REF_ID` | [WORKING_VIEW](WORKING_VIEW.md) | `WORKING_VIEW_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

