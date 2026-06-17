# MEDIA

> The Media table contains information specific to alternate types of radiology media. (ex. Video tape, Cine, CD, etc.)

**Description:** Media  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTINUE_TAPE_ID` | DOUBLE | NOT NULL |  | The Continue_Tape_Id contains the unique id for the video tape that an exams recording has been continued on to. This may or may not be filled out. |
| 2 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Image_Class table. This uniquely identifies a specific media item. |
| 3 | `TAPE_TYPE_CD` | DOUBLE | NOT NULL |  | The Tape_Type_Cd identifies what type of video tape it is. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQ_OBJECT_ID` | [IMAGE_CLASS](IMAGE_CLASS.md) | `SEQ_OBJECT_ID` |

