# PCS_LAYOUT_GROUP

> This table identifies groups of events to be filled in sequence withing the result layout.

**Description:** PathNet Common Services Layout Group  
**Table type:** REFERENCE  
**Primary key:** `PCS_LAYOUT_GROUP_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FILL_ORDER_FLAG` | DOUBLE | NOT NULL |  | Indicates the positioning of result events within the format that is applied to the result layout. 0 - Best Fit; 1 - Adjacent |
| 5 | `GROUP_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The sequence in which the result sets for the fill group is added to the result layout. |
| 6 | `PCS_LAYOUT_GROUP_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a group of events to be filled in sequence within the result layout. |
| 7 | `PCS_RSLT_LAYOUT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related result layout. |
| 8 | `PREV_PCS_LAYOUT_GROUP_ID` | DOUBLE | NOT NULL |  | Used to track versions of the PCS Layout Group information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `SEPARATOR_IND` | DOUBLE |  |  | Indicates whether a separator is needed between this fill group and the next in the formatting applied to the result layout. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCS_RSLT_LAYOUT_ID` | [PCS_RSLT_LAYOUT](PCS_RSLT_LAYOUT.md) | `PCS_RSLT_LAYOUT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCS_LAYOUT_GROUP_EVENT](PCS_LAYOUT_GROUP_EVENT.md) | `PCS_LAYOUT_GROUP_ID` |

