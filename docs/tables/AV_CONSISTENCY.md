# AV_CONSISTENCY

> Stores autoverification consistency parameters.

**Description:** Autoverification Consistency  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AV_CONSISTENCY_FLAG` | DOUBLE | NOT NULL |  | Defines the type of result flag (such as Reference, Critical, Linear, and so on) to which this row of consistency parameters applies. |
| 3 | `AV_REF_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific autoverification reference row associated with the consistency parameters. Creates a relationship to the autoverify reference table. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CONSISTENCY_IND` | DOUBLE | NOT NULL |  | Indicates whether consistency checking is turned on or off. |
| 6 | `CONSISTENCY_MINUTES` | DOUBLE | NOT NULL |  | Defines the number of minutes in which a result must be entered in order to be checked for consistency. |
| 7 | `CONSISTENCY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defines the type of consistency checking (such as percent or absolute) that will be performed. |
| 8 | `CONSISTENCY_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific unit of time in which the Consistency_Minutes column was defined originally. This can equate to either hours or minutes. |
| 9 | `CONSISTENCY_VARIANCE` | DOUBLE | NOT NULL |  | Defines the result variance within which a previous result must be to pass consistency checking. This is either an absolute value or a percentage. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AV_REF_ID` | [AUTO_VERIFY](AUTO_VERIFY.md) | `AV_REF_ID` |

