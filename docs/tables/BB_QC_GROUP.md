# BB_QC_GROUP

> This table maintains a list of Blood Bank quality control groups.

**Description:** Blood Bank Quality Control Group  
**Table type:** REFERENCE  
**Primary key:** `GROUP_ID`  
**Columns:** 15  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `GROUP_DESC` | VARCHAR(60) | NOT NULL |  | This field contains the long description for the quality control group. |
| 3 | `GROUP_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies the quality control group. |
| 4 | `GROUP_NAME` | VARCHAR(40) | NOT NULL |  | This field contains the short display name for the quality control group. |
| 5 | `GROUP_NAME_KEY` | VARCHAR(40) | NOT NULL |  | This field contains the same data as the group name column only it is converted to uppercase. |
| 6 | `GROUP_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | GROUP_NAME_KEY_A_NLS column |
| 7 | `GROUP_NAME_KEY_NLS` | VARCHAR(82) | NOT NULL |  | This field contains the same data as the group_name_key only stored in the corresponding non-English character set values for _KEY. |
| 8 | `REQUIRE_VALIDATION_IND` | DOUBLE | NOT NULL |  | This field indicates if the user will be required to validate the lot numbers for each scheduled quality control entry. |
| 9 | `SCHEDULE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the associated schedule code. |
| 10 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the associated service resource code. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BB_QC_GROUP_ACTIVITY](BB_QC_GROUP_ACTIVITY.md) | `GROUP_ID` |
| [BB_QC_GROUP_ACTIVITY](BB_QC_GROUP_ACTIVITY.md) | `RELATED_GROUP_ID` |
| [BB_QC_GROUP_XREF](BB_QC_GROUP_XREF.md) | `GROUP_ID` |
| [BB_QC_GROUP_XREF](BB_QC_GROUP_XREF.md) | `RELATED_GROUP_ID` |
| [BB_QC_GRP_REAGENT_LOT](BB_QC_GRP_REAGENT_LOT.md) | `GROUP_ID` |
| [BB_WORKLIST](BB_WORKLIST.md) | `QC_GROUP_ID` |
| [RESULT](RESULT.md) | `BB_GROUP_ID` |

