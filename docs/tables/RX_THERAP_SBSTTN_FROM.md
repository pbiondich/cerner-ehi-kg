# RX_THERAP_SBSTTN_FROM

> Medication therapeutic substitution reference data for a drug that a substitution has been created.

**Description:** Therapeutic Substitution From  
**Table type:** REFERENCE  
**Primary key:** `THERAP_SBSTTN_FROM_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 3 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row isr valid as active current data. This may be valued with the date that the row will become inactive. |
| 4 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Link to any text to be shown during the substitution alert. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Allows facility level flexing of substitutions. |
| 7 | `FROM_CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Order catalog code from the ORDER_CATALOG table. Identifies the row as defining a substitution at the catalog level. |
| 8 | `FROM_DRUG_FORM_CD` | DOUBLE | NOT NULL |  | The drug form that is on the original from synonym to be substituted. |
| 9 | `FROM_FREQ_CD` | DOUBLE | NOT NULL |  | Ordered frequency must match to qualify for the substitution. |
| 10 | `FROM_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Product item id from the MEDICATION_DEFINITION table. Identifies the row as defining a substitution at the product level. |
| 11 | `FROM_RTE_CD` | DOUBLE | NOT NULL |  | Ordered route must match to qualify for the substitution. |
| 12 | `FROM_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Ordered dose must match to qualify for the substitution. |
| 13 | `FROM_STRENGTH_VALUE` | DOUBLE | NOT NULL |  | Premise dose strength. Ordered dose must match to qualify for the substitution. |
| 14 | `FROM_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Order catalog synonym id from the ORDER_CATALOG_SYNONYM table. Identifies the row as defining a substitution at the synonym level. |
| 15 | `FROM_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Ordered dose must match to qualify for the substitution. |
| 16 | `FROM_VOLUME_VALUE` | DOUBLE | NOT NULL |  | Ordered dose must match to qualify for the substitution. |
| 17 | `RETAIN_DETAILS_IND` | DOUBLE | NOT NULL |  | Specifies if details specified with the ordered item but not defined on the substituted item will be brought forward with the substitution. 0 = No, 1 = Yes. |
| 18 | `SBSTTN_ACTN_FLAG` | DOUBLE | NOT NULL |  | Defines whether the substitution is automatic, required with notification or optional/decided by the user. |
| 19 | `THERAP_SBSTTN_FROM_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_THERAP_SBSTTN_FROM table. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `VENUE_CD` | DOUBLE | NOT NULL |  | Identifies the venue in which the substitution will be used such as Inpatient, Ambulatory, Discharge Meds, etc. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `FROM_CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `FROM_ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `FROM_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_THERAP_SBSTTN_TO](RX_THERAP_SBSTTN_TO.md) | `THERAP_SBSTTN_FROM_ID` |

