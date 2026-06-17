# TERM

> Each row in the Term table represents a special form of a string, eg. eponym, acronym, tradename, laboratory number, etc. For English language entries, each string is linked to all of its lexical variants or minor variations by means of a common term ide

**Description:** Term  
**Table type:** REFERENCE  
**Primary key:** `TERM_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONCEPT_IDENTIFIER` | VARCHAR(242) |  |  | A unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a concept. All Cerner assigned concept identifiers are created from the CONCEPT_SEQ. The sequence number is formatted to an 8-byte number padded |
| 7 | `CONCEPT_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents the external source that owns the concept_identifier. |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `TERM_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the term table. It is an internal system assigned number. |
| 13 | `TERM_IDENTIFIER` | CHAR(18) |  |  | A unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a term. |
| 14 | `TERM_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents the external source that owns the term_identifier. |
| 15 | `TERM_STATUS_CD` | DOUBLE | NOT NULL |  | Indication of whether the term is the preferred name of the concept or a synonym. Each language has its own preferred term. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [NOMENCLATURE](NOMENCLATURE.md) | `TERM_ID` |

