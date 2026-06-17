# MIC_STAT_SUS_GROUP_NUMERIC

> This statistical reference table contains the numeric results grouping information based on susceptibility group criteria. This is a child table of mic_stat_sus_group.

**Description:** Micro Susceptibility Group Numeric Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_RANGE` | DOUBLE | NOT NULL |  | This field indicates the beginning value in the range. This value cannot exceed the maximum value defined for the numeric susceptibility detail. |
| 2 | `END_RANGE` | DOUBLE | NOT NULL |  | This field indicates the ending value in the range. This value cannot exceed the maximum value defined for the numeric susceptibility detail. |
| 3 | `GROUP_CD` | DOUBLE | NOT NULL |  | This field indicates the code_value of the group name. |
| 4 | `SUS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains a foreign key value used to join sus group information stored on mic_stat_sus_dc_group table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SUS_GROUP_ID` | [MIC_STAT_SUS_GROUP](MIC_STAT_SUS_GROUP.md) | `SUS_GROUP_ID` |

