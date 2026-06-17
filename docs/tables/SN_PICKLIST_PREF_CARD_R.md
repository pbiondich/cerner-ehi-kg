# SN_PICKLIST_PREF_CARD_R

> Preference Cards used in the generation of the picklist

**Description:** Surginet Picklist Preference Card Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDED_DT_TM` | DATETIME |  |  | The date and time the prefernce card was added to the picklist |
| 2 | `CATALOG_CD` | DOUBLE |  | FK→ | The procedure code that caused the preference card to be used for the picklist. Only populated if sn_pref_card_id is populated. |
| 3 | `POST_GENERATION_IND` | DOUBLE | NOT NULL |  | Inidcates that the Preference Card was added to the picklist manually, after the picklist was automatically generated |
| 4 | `PREF_CARD_ID` | DOUBLE | NOT NULL | FK→ | Preference Card Id used to generate the picklist |
| 5 | `SN_PICKLIST_ID` | DOUBLE | NOT NULL | FK→ | The related Surginet Picklist id; |
| 6 | `SN_PICKLIST_PREF_CARD_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `SN_PREF_CARD_ID` | DOUBLE |  | FK→ | A foreign key to the sn_pref_card table. This field will be zero or null if the pref_card_id fild is populated. the pref_card_id OR the sn_pref_card_id should be filled out (which one is filled out will tell us which model - old or new - was used for the given picklist) |
| 8 | `SURGEON_ID` | DOUBLE |  | FK→ | The surgeon associated to the procedure for the prerence card. Used for exception logic. Only applies if sn_pref_card_id is populated. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `USER_SELECTED_IND` | DOUBLE |  |  | Indicates if the user manually selected the preference card to be used instead of using the system defined preference card |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |
| `SN_PICKLIST_ID` | [SN_PICKLIST](SN_PICKLIST.md) | `SN_PICKLIST_ID` |
| `SN_PREF_CARD_ID` | [SN_PREF_CARD](SN_PREF_CARD.md) | `SN_PREF_CARD_ID` |
| `SURGEON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

