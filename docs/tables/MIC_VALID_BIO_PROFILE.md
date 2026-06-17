# MIC_VALID_BIO_PROFILE

> This reference table defines whether block/profile and percent positive data has been built for a group biochemical.

**Description:** Microbiology Valid Biochemical Profile  
**Table type:** REFERENCE  
**Primary key:** `GROUP_BIOCHEMICAL_CD`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOCK_PROFILE_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the block/profile data built for a group biochemical is complete. Block/profile data is not considered complete until block/profile values have been entered for ALL detail biochemicals for a specific group biochemical. |
| 2 | `GROUP_BIOCHEMICAL_CD` | DOUBLE | NOT NULL | PK | This field identifies the code value associated with the group biochemical. |
| 3 | `PERCENT_POSITIVE_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the percent positive data built for a group biochemical is complete. Percent positive data is not considered complete until ALL percent positive values have been entered for organism/detail biochemical combinations. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_BIO_BLOCK_PROFILE](MIC_BIO_BLOCK_PROFILE.md) | `GROUP_BIOCHEMICAL_CD` |

