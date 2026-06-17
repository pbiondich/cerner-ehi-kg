# MP_MPAGE_DEF

> Base information about an MPage. Used by MPage Definition Manager application and the Specialty Experience Manager.

**Description:** Mpage Definition  
**Table type:** REFERENCE  
**Primary key:** `MP_MPAGE_DEF_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Contains the application number that the definition is associated with. |
| 2 | `DEF_TYPE_FLAG` | DOUBLE | NOT NULL |  | This flag will distinguish which application (Definition Manager/Specialty Manager) is using saved record/definition. |
| 3 | `DISPLAY_TXT` | VARCHAR(100) | NOT NULL |  | Display string for the MPages definition. |
| 4 | `DRIVER_SCRIPT_NAME` | VARCHAR(255) | NOT NULL |  | The script that controls the rendering of the MPage. |
| 5 | `MPAGE_MEANING` | VARCHAR(30) | NOT NULL |  | A short description of the MPage |
| 6 | `MP_MPAGE_DEF_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MP_MPAGE_DEF table. |
| 7 | `PARAMETER_TXT` | VARCHAR(255) | NOT NULL |  | The parameters used by the driver script when rendering the MPage. |
| 8 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position code of the user at the time the row was created. |
| 9 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Used in Specialty Manager. The person for which the definition was saved. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `VIEW_SEQ` | DOUBLE | NOT NULL |  | Specialty Manager saves the definition for specific PowerChart tabs(Org/Chart level). view_seq will be used to identify that tab. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MP_MPAGE_GROUP_RELTN](MP_MPAGE_GROUP_RELTN.md) | `MP_MPAGE_DEF_ID` |

