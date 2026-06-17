# MLTM_FREQUENCY

> This table contains a listing of Multum's frequency of administration terms, along with an abbreviation and a unique identifier for each term.

**Description:** Multum frequency  
**Table type:** REFERENCE  
**Primary key:** `FREQUENCY_CODE`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FREQUENCY_ABBR` | VARCHAR(10) |  |  | This field contains an abbreviation for the frequency of administration. For example, the frequency abbreviation for the frequency description every 4 hours is Q4H. This field is most appropriate for applications where such terms are commonly used by healthcare professionals. |
| 2 | `FREQUENCY_CODE` | DOUBLE | NOT NULL | PK | This field contains a numeric identifier assigned to a frequency of administration. A unique identifier for rows in this table. |
| 3 | `FREQUENCY_DESCRIPTION` | VARCHAR(255) |  |  | This field contains a full text description of the frequency of administration for a drug and includes specific terms such as every 4 hours or 4 times daily. This field is most appropriate for applications that use full text descriptions for clarity or for presentation to non-professional personnel. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_SCRIPT_COMMON](MLTM_SCRIPT_COMMON.md) | `FREQUENCY_CODE` |

