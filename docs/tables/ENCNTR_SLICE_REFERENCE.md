# ENCNTR_SLICE_REFERENCE

> Relationship of the ENCOUNTER SLICE type and the SCHEDULE FLEX RULE that defines it.

**Description:** Encounter Slice Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACP_IND` | DOUBLE | NOT NULL |  | Indicates which slice owns the augmented care periods. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CODING_IND` | DOUBLE | NOT NULL |  | An indicator for which slice owns the Profile coding. |
| 8 | `COMMISSIONING_IND` | DOUBLE | NOT NULL |  | Indicates which slice owns the EEM Commission. |
| 9 | `DATE_RANGE_LOCK_IND` | DOUBLE | NOT NULL |  | Indicator to determine if the user can modify a slice row before the slice_start_field or after the slice_end_field value. If this is true then we will not let them update the values past that range, if it is false we will just warn them. |
| 10 | `ENCNTR_SLICE_REF_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the relation of the encounterslice type and the schedule flex rule that defines it. |
| 11 | `ENCNTR_SLICE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of encounter slice. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `END_ENCNTR_COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Contains the name of the column on the encounter table that contains the end date and time corresponding to the date range in which a slice can be modified. |
| 14 | `FROM_ED_IND` | DOUBLE | NOT NULL |  | Indicates whether this encounter was transferred from the emergency department. |
| 15 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | This column relates the encounter slice rule to a specific entry on the sch_flex_string. |
| 16 | `START_ENCNTR_COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Contains the name of the column on the encounter table that contains the start date and time corresponding to the date range in which a slice can be modified. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

