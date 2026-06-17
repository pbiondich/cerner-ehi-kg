# MIC_STAT_GROUP

> Code set 28020 contains the different Group Types. MIC_STAT_GROUP stores specific groups for an given group type.

**Description:** Stores the Statistical Groupings.  
**Table type:** REFERENCE  
**Primary key:** `STAT_GROUP_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DISPLAY` | VARCHAR(40) | NOT NULL |  | This field contains the display value for the statistical grouping. |
| 3 | `DISPLAY_KEY` | VARCHAR(40) | NOT NULL |  | This field contains the display key which is generated from the display field (converted to Uppercase, with all spaces and special characters removed). |
| 4 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code that uniquely identifies the type of statistical grouping (i.e. age days, encounter type, medical service, ...). |
| 5 | `STAT_GROUP_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the statistical grouping (and its associated parameters). This value is used to join to other tables, such as the MIC_STAT_GROUP_DETAIL table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_STAT_GROUP_DETAIL](MIC_STAT_GROUP_DETAIL.md) | `STAT_GROUP_ID` |

