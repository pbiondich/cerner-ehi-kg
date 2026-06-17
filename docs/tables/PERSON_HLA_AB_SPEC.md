# PERSON_HLA_AB_SPEC

> Defines specific antibodies identified for a person during HLA antibody screening over time.

**Description:** Person HLA Antibody Specificity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HLA_AB_SCREEN_ID` | DOUBLE | NOT NULL | FK→ | Relates the Antibody Screen Specificity History to a manually entered Antibody Screen History record. Not populated when history is automatically generated. |
| 2 | `HLA_AB_SPEC_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies an HLA Antibody Screen Specificity history record. |
| 3 | `HLA_TYPE_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the antibody determined by an Antibody Screen. Either derived from Antibody Screen results or entered manually into history. |
| 4 | `MAP_AB_DTA_CD` | DOUBLE |  |  | Reference to ab_dta_cd on the hla_ab_spec_map table. This records the mapping record used to create the person_hla_ab_spec record. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates results for the HLA Typing tray to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HLA_AB_SCREEN_ID` | [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `HLA_AB_SCREEN_ID` |
| `HLA_TYPE_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

