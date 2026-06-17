# STICKY_NOTE

> Stores different types of sticky notes, notes that can be 'stuck' to any entity

**Description:** Sticky Note  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This is the id to the long text table, If the note is too long to fit on the sticky note table it will be written to the long text table and referenced here. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary index of the row in the table that the sticky note is 'stuck' to. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | The table name that the sticky note is 'stuck' to. (i.e. PERSON) |
| 6 | `PUBLIC_IND` | DOUBLE |  |  | Indicator specifying whether note is public to view, printable on reports, or any other similar use |
| 7 | `STICKY_NOTE_ID` | DOUBLE | NOT NULL |  | The unique, primary index for a row on the table |
| 8 | `STICKY_NOTE_STATUS_CD` | DOUBLE | NOT NULL |  | Status of note for purging purposes |
| 9 | `STICKY_NOTE_TEXT` | VARCHAR(255) |  |  | the text 'on' the sticky note |
| 10 | `STICKY_NOTE_TYPE_CD` | DOUBLE | NOT NULL |  | This distiguishes the types of sticky notes (i.e. powerchart's vs. profile's) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

