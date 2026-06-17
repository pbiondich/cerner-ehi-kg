# AP_SYNOPTIC_SPEC_PREFIX_R

> This reference table defines the association between AP synoptic worksheets and specimen/prefix combinations. This relationship is used to determine which synoptic worksheets can be resulted for a pathology case/specimen type combination.

**Description:** AP Synoptic Worksheet Specimen Prefix Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CKI_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | External identifier for the AP synoptic worksheet, used with the CKI_SOURCE column to form a unique external identifier. |
| 2 | `CKI_SOURCE` | CHAR(12) | NOT NULL |  | External source for the AP synoptic worksheet, used with CKI_IDENTIFIER to form a unique external identifier. |
| 3 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the prefix to which synoptic worksheets are defined. It is valid for this column to be zero when synoptic worksheets are defined at the specimen level only. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field defines the sequence for synoptic worksheets associates with a specimen/prefix combination. |
| 5 | `SPECIMEN_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value for the AP specimen. The combinations of the specimen_cd and prefix_id columns are used to define valid synoptic worksheets. |
| 6 | `SUGGESTED_FLAG` | DOUBLE | NOT NULL |  | This field defines whether the synoptic worksheet is allowed or suggested. Suggested indicates that the worksheet will automatically be defaulted in for entry when a pathology case is accessioned for a given prefix/specimen combination. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |
| `SPECIMEN_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

