# DD_EMR_EXTRACT

> Stores XML containing details behind chart data referenced in Dynamic Documentation notes.

**Description:** Dynamic Documentation Electronic Medical Record Extract  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DD_CONTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | The contribution containing the EMR content place holder described by this XML |
| 2 | `DD_EMR_EXTRACT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies stored XML data which comtains details behind chart data referenced in Dynamic Documentation notes. |
| 3 | `EXTRACT_UUID` | VARCHAR(255) | NOT NULL |  | Identifies EMR content place holder in the contribution described by this XML. |
| 4 | `EXTRACT_XML_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the long_blob record that contains XML returned by MSVC data extraction services. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_CONTRIBUTION_ID` | [DD_CONTRIBUTION](DD_CONTRIBUTION.md) | `DD_CONTRIBUTION_ID` |
| `EXTRACT_XML_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

