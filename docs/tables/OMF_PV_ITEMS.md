# OMF_PV_ITEMS

> PowerVision items such as Saved Views, Fitlers, and Templates.

**Description:** OMF PV ITEMS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_PROMPT_IND` | DOUBLE | NOT NULL |  | Determines if we prompt for filterings when running. |
| 2 | `FOLDER_ID` | DOUBLE |  |  | PowerVision folder that this item is stored in. |
| 3 | `GRID_CD` | DOUBLE | NOT NULL |  | Subject area this item belongs to. Other codesets can be used besides 14265 depending on the team defining the value. |
| 4 | `ITEM_TYPE_FLAG` | DOUBLE | NOT NULL |  | PowerVision item type such as Saved View, Template and Filter. |
| 5 | `OMF_PV_ITEM_ID` | DOUBLE | NOT NULL |  | Unique identifier of the PV item. |
| 6 | `PROGRAM_GROUP_NBR` | DOUBLE |  |  | If the item is a Discern Explorer (CCL) program, this field contains the program group associated with the CCL program. This should match the object group shown in CCLProt. |
| 7 | `PROGRAM_NAME_TXT` | VARCHAR(30) |  |  | If the item is a Discern Explorer (CCL) program, this field contains the name of the Discern Explorer program associated with the item. |
| 8 | `PROP_PROMPT_IND` | DOUBLE | NOT NULL |  | Determines whether we prompt for properties when running the Saved View. |
| 9 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | If the item is associated with a 'User Group' rather than a user, this field contains the internal surrogate value which identifies the group. |
| 10 | `PV_ITEM_NAME` | VARCHAR(255) | NOT NULL |  | Name of PowerVision item. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `USER_ID` | DOUBLE | NOT NULL |  | Person who owns this PowerVision item. |
| 17 | `VIEW_CD` | DOUBLE | NOT NULL |  | View which this item belongs to. Other codesets can be used besides 14265 depending on the team defining the value. |
| 18 | `VIEW_TYPE` | DOUBLE | NOT NULL |  | Type of viewer which this was saved for. List of possible viewers is stored in omf_pv_viewers. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

