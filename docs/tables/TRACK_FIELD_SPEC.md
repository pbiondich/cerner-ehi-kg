# TRACK_FIELD_SPEC

> Reference data describing a field of tracking data

**Description:** Tracking Field Specification  
**Table type:** REFERENCE  
**Primary key:** `TRACK_FIELD_SPEC_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIGNMENT_FLAG` | DOUBLE | NOT NULL |  | Alignment Flag. 0= LEFT, 1= CENTER, 2= RIGHT |
| 2 | `ASCENDING_IND` | DOUBLE | NOT NULL |  | If SORTING_SEQ is non-negative, this field indicates whether sorting should be ascending or descending |
| 3 | `BEHAVIOR_BIT_MAP` | DOUBLE | NOT NULL |  | A bitmask that configures the way this field will behave. |
| 4 | `DISPLAY_TXT` | VARCHAR(64) | NOT NULL |  | Field Display |
| 5 | `DISPLAY_WIDTH` | DOUBLE | NOT NULL |  | Width in pixels available for this field |
| 6 | `FIELD_ENUM` | DOUBLE | NOT NULL |  | Defines what type of field this is. a unique number on the front end that defines what type of field this is. Both field_enum and interaction_enum are extensible concepts, in that we can add new implementations at any time. |
| 7 | `FIELD_SEQ` | DOUBLE | NOT NULL |  | The order of this field in the field list. Can be -1 if this field is for sorting only, not for display |
| 8 | `INTERACTION_ENUM` | DOUBLE | NOT NULL |  | Defines what type of Interaction this is. a unique number on the front end that defines the Interaction. Both field_enum and interaction_enum are extensible concepts, in that we can add new implementations at any time. |
| 9 | `READ_ONLY_IND` | DOUBLE | NOT NULL |  | Indicates whether a column on the front end is to be a Read Only column. A 0 means the column is not read only (default). A 1 would indicate that the column should be read only. |
| 10 | `SORTING_SEQ` | DOUBLE | NOT NULL |  | The order in which this field will be sorted. Can be -1 if this field is not sorted upon. |
| 11 | `TRACK_FIELD_SPEC_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 12 | `TRACK_VIEW_FIELD_LIST_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from TRACK_VIEW_FIELD_LIST |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `WRAP_IND` | DOUBLE | NOT NULL |  | Wrap Indicator - default is 0. 1 = if the text field should wrap to fit the column width. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_VIEW_FIELD_LIST_ID` | [TRACK_VIEW_FIELD_LIST](TRACK_VIEW_FIELD_LIST.md) | `TRACK_VIEW_FIELD_LIST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [TRACK_FIELD_SPEC_BEHAVIOR](TRACK_FIELD_SPEC_BEHAVIOR.md) | `TRACK_FIELD_SPEC_ID` |
| [TRACK_FIELD_SPEC_REFINEMENT](TRACK_FIELD_SPEC_REFINEMENT.md) | `TRACK_FIELD_SPEC_ID` |

