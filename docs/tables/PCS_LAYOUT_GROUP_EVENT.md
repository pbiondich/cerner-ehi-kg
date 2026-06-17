# PCS_LAYOUT_GROUP_EVENT

> This table identifies event codes contained within a fill gorup and the sequence they are filled within the result layout.

**Description:** PathNet Common Services Layout Group Event  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EVENT_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the event code to fill into the result layout. |
| 5 | `EVENT_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The sequence in which the event code will appear within a result set for the fill group it is in. |
| 6 | `PCS_LAYOUT_GROUP_EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies event codes contained within a fill group and the sequence they are filled within the result layout. |
| 7 | `PCS_LAYOUT_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the result layout fill group the event code is in. |
| 8 | `PREV_PCS_LAYOUT_GROUP_EVENT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the PCS Layout Group Event information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCS_LAYOUT_GROUP_ID` | [PCS_LAYOUT_GROUP](PCS_LAYOUT_GROUP.md) | `PCS_LAYOUT_GROUP_ID` |

