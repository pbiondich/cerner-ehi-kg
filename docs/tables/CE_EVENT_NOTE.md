# CE_EVENT_NOTE

> The Event Note table stores any comments associated with the event. Typically this would include additional information about reference ranges, or notes indicating that the result value has been changed from a previous result.

**Description:** ce event note  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_EVENT_NOTE_ID` | DOUBLE | NOT NULL |  | Unique identifier generated for each row of data |
| 2 | `CHECKSUM` | DOUBLE | NOT NULL |  | A unique value, created by parsing the contents of the blob, used as a comparison to identify changes to the blob. |
| 3 | `COMPRESSION_CD` | DOUBLE | NOT NULL |  | Specifies type of compression applied to the blob. |
| 4 | `ENTRY_METHOD_CD` | DOUBLE | NOT NULL |  | Source of note. Ancillary/Owner application, Orderer/Provider, Medical Records ManagerCode. |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the event table. |
| 6 | `EVENT_NOTE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical event note row. There may be more than one row with the same event_note_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field |
| 7 | `IMPORTANCE_FLAG` | DOUBLE |  |  | Indicates the importance of this note |
| 8 | `LONG_TEXT_ID` | DOUBLE |  |  | Id of long text row containing note |
| 9 | `NON_CHARTABLE_FLAG` | DOUBLE |  |  | If true, this event note is not chartable. |
| 10 | `NOTE_DT_TM` | DATETIME | NOT NULL |  | Date/Time of note entry. |
| 11 | `NOTE_FORMAT_CD` | DOUBLE | NOT NULL |  | Indicates type of blob. Note that a storage code doesn¿t exist - all blobs must exist on the long_blob table. Thus only format codes that apply to the storage code BLOB are valid here. |
| 12 | `NOTE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel id of person who wrote the note. Foreign key to Personnel table. |
| 13 | `NOTE_TYPE_CD` | DOUBLE | NOT NULL |  | Type of notes: 7 Reason for insertion of an external apparatus 7 Reason for Deferring a medication administration 7 Complication Code 7 Cancel Reason 7 Delete Reason 7 Deferred Reason 7 Clinical Note 7 Instrument Flag for Lab 7 Complication Code for External Apparatus 7 Medication Administration Instruction. 7 Patient Follow-up/Reaction Comments. We need to determine whether to have a general "Delete Reason" note type for all result type, or different ones . |
| 14 | `NOTE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 15 | `RECORD_STATUS_CD` | DOUBLE | NOT NULL |  | Record status code. Values: active, inactive, deleted combined away, needs review. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 22 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the End Point of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

