# MLTM_SEVERITY

> This table defines severity level for clinical text, such as a drug interaction.

**Description:** Multum Severity  
**Table type:** REFERENCE  
**Primary key:** `SEVERITY_ID`  
**Columns:** 7  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SEVERITY_DESCRIPTION` | VARCHAR(50) |  |  | This field contains a textual description of the potential severity of a drug interaction, pregnancy alert, or lactation alert, as well as an indication that general warning or contraindication text is not applicable to a particular drug. |
| 2 | `SEVERITY_ID` | DOUBLE | NOT NULL | PK | The PK column for this table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MLTM_INT_HEADER_SEVERITY_MAP](MLTM_INT_HEADER_SEVERITY_MAP.md) | `SEVERITY_ID` |
| [MLTM_XP_CLIN_TEXT_XREF](MLTM_XP_CLIN_TEXT_XREF.md) | `SEVERITY_ID` |

